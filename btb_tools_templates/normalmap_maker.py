import numpy
import scipy.ndimage as ndi
import imageio
import argparse
import matplotlib.pyplot as plt


class NormalMapMaker:
    intensity=1
    sig=0

    def sgauss(self,im):
        if self.sig==0:
            return im
        im_sm = im.astype(float)
        kx= numpy.arrange(-3*sig,3*sig+1).astype(float)
        kx= numpy.exp((-(kx**2))/(2*(sig**2)))
        im_sm=ndi.convolve(im_sm,kx[numpy.newaxis])
        im_sm=ndi.convolve(im_sm,kx[numpy.newaxis].T)
        return im_sm

    def grad(self,im_sm):
        gradx = im_sm.astype(float)
        grady = im_sm.astype(float)
        k= numpy.arange(-1,2).astype(float)
        k= -k/2
        gradx = ndi.convolve(gradx, k[numpy.newaxis])
        grady = ndi.convolve(grady, k[numpy.newaxis].T)
        return gradx,grady

    def sbl(self,im_sm):
        gradx = im_sm.astype(float)
        grady = im_sm.astype(float)
        k = numpy.array([[-1,0,1],[-2,0,2],[-1,0,1]])
        gradx = ndi.convolve(gradx, k)
        grady = ndi.convolve(grady, k.T)
        return gradx,grady

    def comp_nm(self,gradx, grady):
        width = gradx.shape[1]
        height = gradx.shape[0]
        max_x = numpy.max(gradx)
        max_y = numpy.max(grady)
        max_value = max_x
        if max_y > max_x:
            max_value = max_y
        normal_map = numpy.zeros((height, width, 3), dtype=numpy.float32)
        #self.intensity = 1 / self.intensity
        strength = max_value / (max_value * self.intensity)
        normal_map[..., 0] = gradx / max_value
        normal_map[..., 1] = grady / max_value
        normal_map[..., 2] = 1 / strength
        norm = numpy.sqrt(numpy.power(normal_map[..., 0], 2) + numpy.power(normal_map[..., 1], 2) + numpy.power(normal_map[..., 2], 2))
        normal_map[..., 0] /= norm
        normal_map[..., 1] /= norm
        normal_map[..., 2] /= norm
        normal_map *= 0.5
        normal_map += 0.5
        return normal_map

    def diffuse_to_normal(self, diffuse_path):
        new_path=diffuse_path.replace("Diffuse.png","Normal.png")
        return new_path

    def make_normal(self,diffuse_path):
        try:
            img= plt.imread(diffuse_path)
            if img.ndim == 3:
                img_grey = numpy.zeros((img.shape[0],img.shape[1])).astype(float)
                img_grey = (img[...,0] * 0.3 + img[...,1] * 0.6 + img[...,2] * 0.1)
                img = img_grey
            img_smooth = self.sgauss(img)
            sblx, sbly = self.sbl(img_smooth)
            normal_map = self.comp_nm(sblx, sbly)
            imageio.imwrite(self.diffuse_to_normal(diffuse_path), normal_map)
        except:
            print("FAILED TO MAKE NORMAL IMAGE")

#if __name__ == "__main__":
#    main()

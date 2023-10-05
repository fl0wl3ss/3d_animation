from mayavi import mlab
import numpy as np
import os

# load exp results
loaded_data = np.load('asym_demo.npz')
data = loaded_data['data']
print(np.shape(data))
num_steps, num_x, num_y = data.shape

# options
output_directory = "output_frames"
mlab.figure(size=(800, 600))
x, y = np.mgrid[-2:2:128j, -2:2:128j]

# define animation function 
def anim():
    @mlab.animate(delay=100)
    def update():
        for step in range(num_steps):
            # generate frame data
            frame_data = data[step]

            # create surf plot
            #surf = mlab.surf(x, y, frame_data, colormap='viridis', warp_scale="auto")
            surf = mlab.surf(x, y, frame_data, colormap='viridis', warp_scale=1 , vmin=0, vmax=1)
            colorbar = mlab.colorbar(surf, nb_labels=0)  # ラベルフォーマットを設定

            # setting a Point of View
            mlab.view(azimuth=45, elevation=45, distance=4, focalpoint=(3, 3, 4))

            yield

            # save video frame
            filename = os.path.join(output_directory, f"frame_{step:04d}.png")
            mlab.savefig(filename)
            
            # remove sur plot to next loop
            surf.remove()
            colorbar.visible = False  

    anim = update()
    mlab.show()
    return anim

# start animation
animation = anim()

# GUI controls animation
@mlab.show
def gui_callback():
    animation.play()

mlab.show()


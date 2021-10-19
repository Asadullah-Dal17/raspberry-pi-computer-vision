# Basics Setup and Testing USB cameara on pi

## Installation 

### Install FFMPEG

```
sudo apt install ffmpeg
```

### Install Opencv, on python3 

```
sudo apt install python3-opencv
```
⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️
> ⚠️Note: FFmpeg and OpenCV from official repository have been built with less optimisations. It is recommended to build from sources with the *supported optimisations* ⚠️

### Install dependency packages
```pip 
sudo apt install libxcb-shm0 libcdio-paranoia-dev libsdl2-2.0-0 libxv1  libtheora0 libva-drm2 libva-x11-2 libvdpau1 libharfbuzz0b libbluray2 libatlas-base-dev libhdf5-103 libgtk-3-0 libdc1394-22 libopenexr23
```

### Install Mediapipe for Raspberry Pi4️⃣ 

```pip
sudo pip3 install mediapipe-rpi4

```
pip offical page for [sources](https://pypi.org/project/mediapipe-rpi4/)
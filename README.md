# Climate-Change-AI-Flood

This is a part of the project on Cycle-GAN implementation to visualize the effects of climate change which is initiated by Prof.Yoshua Bengio of MILA, Canada (https://mila.quebec/en/person/bengio-yoshua/). Here we use a pretrained CycleGAN model using PyTorch to generate floods on street view images and display the results using a Python-based web application. 

## CycleGAN 

We use the CycleGAN implementation available in https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix. 

### Prerequisites for CycleGAN
- Linux or MacOS
- Python 3
- CPU or Nvidia GPU + CUDA CuDNN

### Changes to the original CycleGAN

We changed several parameters of the original code to use for visualization. 
- under options/base_options.py, we change --name parameter for the pretrained models
- under options/base_options.py, --model parameter is set to test. --load_size and --crop_size parameters are set to 512. --gpu_ids is set to -1 to use CPU for testing. (Can change it if a GPU is used for testing)

## Getting Started
### Installation

#### CycleGAN
Install all the requirements related to CycleGAN implementation. 

#### Web Application
Install Flask, dominate, GoogleGeocoder, Google Streetview Python API

```bash
$pip install flask
$pip install dominate
$pip install python-googlegeocoder
$pip install google_streetview
```
To use Google Streetview API, get an API key from Google Maps.

### Run the code
Before running the code, change line 8 of app.py to include your Google Maps API key to use Google Streetview. Create a folder named checkpoints in the root directory and include the pretrained models available in this link - https://drive.google.com/drive/folders/1oDzhD-VrobLpjoGeTQ_AqYlQ1w2rI6ql?usp=sharing.

-To run the program
```bash
$python app.py
```
-To view the web application - Use http://127.0.0.1:4555

## Acknowledgements 
The project is initiated by Prof.Yoshua Bengio, his CCAI(Climate Change AI) team and Jennifer Chayes of MSR(Microsoft Research).
CCAI team - Sasha Luccioni (https://sashaluccioni.weebly.com/)
            Kris Sankaran (http://krisrs1128.github.io/personal-site/)
            Victor Schmidt (https://mila.quebec/en/person/vict0rsch/)
            Karthik Mukkavilli (https://www.drawdown.org/fellows/s-karthik-mukkavilli)


<code>
  <h1 align="center">Capture</h1>
</code>
<p align="center">
  Capture is a python based desktop application that lets you capture the text which otherwise cannot be copied. It saves the time spent on software/website to get the text. Just select and voila, your text is copied to the clipboard. It uses python's PyQt5 module for building the entire GUI and pytesseract for extracting text from the image.
</p>
<br>
<br>

<p  align="center"><img width="1000" src = "https://github.com/IshaanOhri/Capture/blob/master/Capture.gif"></p>

<br>

## Installation
1. Prerequisite: [Python 3](https://www.python.org/downloads/)
2. Clone the repo
```
git clone https://github.com/IshaanOhri/Capture.git
```
3. `cd` into directory
```
cd capture
```
4. Install all packages
```
pip install -r requirements.txt
```
5. Run application
```
python app.py
```
If your system default is python 2.x then try running `pip3` and `python3` instead of `pip` and `python`
<br><br>
If you encounter error installing pytesseract, try this:
##### MacOs
```
brew install tesseract
```
##### Linux
```
sudo apt-get install tesseract-ocr
```
##### Windows
Download binary from [here](https://github.com/UB-Mannheim/tesseract/wiki) and add `pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'` to your script
<br><br>
If you continue running into issue refer the INSTALLATION section [here](https://pypi.org/project/pytesseract/)
<br>
The project has been tested only on MacOS, should you encounter any isuue on any other operating system, please feel free to contribute.

<br>

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<br>

## License
The project is distributed under the MIT License. See [LICENSE](https://github.com/IshaanOhri/Capture/blob/master/LICENSE) for more information.

<br>

## Tech stacks used
<p>
  <img src="https://github.com/IshaanOhri/IshaanOhri/blob/master/assets/python.png" height=40 hspace=20>
</p>

<br>

## Inspirational Credits
Thanks to [Ian](https://github.com/ianzhao05) for the inspiration and for the help in code

<br>
<br>
<br>

<p align="center">
  <a href="https://www.linkedin.com/in/ishaanohri/">
    <img src="https://github.com/IshaanOhri/IshaanOhri/blob/master/assets/linkedin.png" width="30" height="30" hspace="20">
  </a>

  <a href="mailto:ishaan99ohri@gmail.com">
    <img src="https://github.com/IshaanOhri/IshaanOhri/blob/master/assets/mail.png" width="30" height="30" hspace="20">
  </a>

  <a href="https://stackoverflow.com/users/11712463/ishaan-ohri">
    <img src="https://github.com/IshaanOhri/IshaanOhri/blob/master/assets/stackoverflow.png" width="30" height="30" hspace="20">
  </a>

  <a href="https://www.instagram.com/ohri_8/">
    <img src="https://github.com/IshaanOhri/IshaanOhri/blob/master/assets/instagram.png" width="30" height="30" hspace="20">
  </a>

  <a href="https://github.com/IshaanOhri">
    <img src="https://github.com/IshaanOhri/IshaanOhri/blob/master/assets/github.png" width="30" height="30" hspace="20">
  </a>
</p>
  
<p align="center">
  <a href="https://github.com/IshaanOhri">
    <img src="https://github.com/IshaanOhri/IshaanOhri/blob/master/assets//ishaan.gif" width="300">
  </a>
</p>

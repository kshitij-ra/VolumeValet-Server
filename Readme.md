<a  name="readme-top"></a>


<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]


<!-- PROJECT LOGO -->
<br />
<div  align="center">
<a  href="https://github.com/kshitij-ra/VolumeValet">
<img  src="images/code.ico"  alt="Logo"  width="80"  height="80">
</a>
<h3  align="center">VolumeValet-Server</h3>
<p  align="center">
VolumeValet is a convenient Android app for controlling your PC's volume from your phone over the local network. This repo is for the VolumeValet-Server that needs to run on your PC.

Check out the [VolumeValet App](https://github.com/kshitij-ra/VolumeValet)
<br />
<a  href="https://github.com/kshitij-ra/VolumeValet-Server/issues">Report Bug</a> · 
<a  href="https://github.com/kshitij-ra/VolumeValet-Server/issues">Request Feature</a>
</p>
</div>

  

  

<!-- TABLE OF CONTENTS -->
<details>
<summary>Table of Contents</summary>
<ol>
<li>
<a  href="#about-the-project">About The Project</a>
<ul>
<li><a  href="#built-with">Built With</a></li>
</ul>
</li>
<li><a  href="#usage">Usage</a></li>
<li>
<a  href="#building-locally">Building Locally/a>
<ul>
<li><a  href="#steps">Steps</a></li>
</ul>
</li>
<li><a  href="#roadmap">Roadmap</a></li>
<li><a  href="#contributing">Contributing</a></li>
<li><a  href="#license">License</a></li>
<li><a  href="#contact">Contact</a></li>
</ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
[![Product Name Screen Shot][product-screenshot]](https://github.com/kshitij-ra/VolumeValet-Server)
  

Whether you're watching a movie, playing a game, or just listening to music, VolumeValet makes it easy to adjust the volume without adjust the volume of your PC without having to reach for the physical controls. Try VolumeValet today and experience the convenience of controlling your PC's volume from your Android phone!

### Features
* Ability to adjust the volume of your PC from your Android phone over the local network.
* Quick mute and unmute functionality.
* Control media playback (pause, play, next, previous).
* Easily connect with PC using QR code.
* Add-free UI.  

<p  align="right">(<a  href="#readme-top">back to top</a>)</p>
  

### Built With 
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)

<p  align="right">(<a  href="#readme-top">back to top</a>)</p>

  
<!-- USAGE EXAMPLES -->
## Usage
  1. Download the precompiled app from [here](https://github.com/kshitij-ra/VolumeValet-Server/releases/tag/v1.0.0) or build the app locally.
  2. Start the server on PC.
  3. Launch the Android app. See [VolumeValet](https://github.com/kshitij-ra/VolumeValet) for details.
  4. Scan the QR or enter the address and port manually.
  5. Press the Connect button.
  6. You are connected!

<p  align="right">(<a  href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Building Locally
### Pre-requesite
Before anything, be sure to have a working python setup. If not installed, go to [BeginnersGuide/Download - Python](https://wiki.python.org/moin/BeginnersGuide/Download).

### Steps
1. Clone the repo  
    ```sh
    $ git clone https://github.com/kshitij-ra/VolumeValet-Server.git
    ```
2. Extract the file and cd to the repo folder.
3. To install dependencies, run 
    ```sh
    $ pip3 install -r requirements.txt
    ```
4. Then run the following in a terminal
    ```sh
    $ python desk.py
    ```

<p  align="right">(<a  href="#readme-top">back to top</a>)</p>  


<!-- ROADMAP -->
## Roadmap  
- [x] Option to scan QR to connect.
- [x] Adopt Material3 Design.
- [x] Control playback (pause, play, next, previous).
- [ ] Integration with Android's accessibility features for users with visual or motor impairments.
- [ ] Option to adjust individual channel volumes for systems with multiple speakers or headphones.
- [ ] Integration with Android's voice assistant, allowing for hands-free volume control.
- [ ] Compatibility for other operating systems.
- [ ] Option to control volume using the volume keys of android device.
- [ ] Create webapp.

<p  align="right">(<a  href="#readme-top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing 

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!  


1. Fork the Project 
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)  
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)  
4. Push to the Branch (`git push origin feature/AmazingFeature`)  
5. Open a Pull Request
  

<p  align="right">(<a  href="#readme-top">back to top</a>)</p>

  

  

<!-- LICENSE -->

  

## License

Distributed under the MIT License. See `LICENSE` for more information.

<p  align="right">(<a  href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Kshitij Radotra - [@kradotra](https://twitter.com/kradotra) - kshitijradotra@gmail.com

Project Link: [https://github.com/kshitij-ra/VolumeValet-Server](https://github.com/kshitij-ra/VolumeValet-Server)

<p  align="right">(<a  href="#readme-top">back to top</a>)</p>  

<!-- ACKNOWLEDGMENTS -->
  

<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/kshitij-ra/VolumeValet-Server.svg?style=for-the-badge
[contributors-url]: https://github.com/kshitij-ra/VolumeValet-Server/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/kshitij-ra/VolumeValet-Server.svg?style=for-the-badge
[forks-url]: https://github.com/kshitij-ra/VolumeValet-Server/network/members
[stars-shield]: https://img.shields.io/github/stars/kshitij-ra/VolumeValet-Server.svg?style=for-the-badge
[stars-url]: https://github.com/kshitij-ra/VolumeValet-Server/stargazers
[issues-shield]: https://img.shields.io/github/issues/kshitij-ra/VolumeValet-Server.svg?style=for-the-badge
[issues-url]: https://github.com/kshitij-ra/VolumeValet-Server/issues
[license-shield]: https://img.shields.io/github/license/kshitij-ra/VolumeValet-Server.svg?style=for-the-badge
[license-url]: https://github.com/kshitij-ra/VolumeValet-Server/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/kshitij-radotra/
[product-screenshot]: images/screenshot.png
[product-logo]: images/code.ico
[Flutter]: https://img.shields.io/badge/Flutter-%2302569B.svg?style=for-the-badge&logo=Flutter&logoColor=white
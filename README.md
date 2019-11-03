**(10/29/19) GUI development starting in new repository!**  Work on transforming BitGlitter from a Python library to an executable with a GUI has begun.  It's been said for a long time on my Discord server that making it accessible to much larger group of people beyond Python devs would help a lot with exposure and getting more momentum, so its a no brainer to make this our next priority.  All future development work will continue here.  The Python library will continue to get all core architecture/performance/protocol updates.  The GUI will be made using PyQt5.  There are also a few planned performance updates to BitGlitter prior to the release of the program.  If you're following this project from the Python library days, be sure to follow this new repo as well.  And as always, come check out our Discord server!

And finally, expect some large changes to happen in this repo in the near future.  The latest version of BitGlitter as a Python library is being used as a starting point to transform it into a GUI.  Excluding the core read/write logic, nearly everything else will be changed prior to release of the executable.  :)

[![Downloads](https://pepy.tech/badge/bitglitter)](https://pepy.tech/project/bitglitter)

**[Discord Server](https://discord.gg/t9uv2pZ)**

![BitGlitter Logo](https://i.imgur.com/3GJ4bDx.png)

# The basics

![BitGlitter Sample GIF](https://i.imgur.com/n7E7lnd.gif)

**[Click here](https://www.youtube.com/watch?v=HrY4deFrOoA) for a demo video of a real stream.**

BitGlitter is an easy to use library that allows you to embed data inside of ordinary pictures or video.  Store and host
files wherever images or videos can be hosted.

### From physical barcodes to digital data transfer

Whether it's barcodes at the store or QR codes you can scan with your phone- they both work on the same principle.  Data
is encoded into the black and white.  You can think of each color as an abstraction for a binary value, so then when
those colors are read in sequence, you can pull meaningful data from the image.  I wondered how this concept could be
improved upon, and I wanted a cool first project as an introduction to programming.  BitGlitter was born.

Conventional barcodes are severely limited in application, in terms of their data density.  When you maximize the 
concept and configure it for digital-digital transmission, a lot of capability is gained.  
BitGlitter is in a class of it's own in several ways:

![BitGlitter Default Palettes](https://i.imgur.com/dSYmq7V.png)

+ **Multiple Color Palettes:**  By removing the constraint of only using black and white, the amount of data you can 
hold in a given "block" (each square) on the frame skyrockets.  The regular two color setup holds one bit per block.  
Four colors holds two  bits (2x), sixty four colors holds six bits (6x), and lossless ~16.7M color palette holds 24 bits 
(24x improvement over black & white).  You choose what color palette you'd like to use according to your application.  
Smaller sets are far resistant to compression and corruption, while larger sets have higher data densities.  You can
create your own custom palettes as well with whatever colors you'd like to use.  More about that below.
+ **Multi-Frame Videos:** BitGlitter automatically breaks up larger files into multiple frames, with several headers
built into them.  These include several layers of protection against corruption, as well as metadata about the frame
as well as the stream itself so the reader can intelligently decide how to handle it.  By stitching these frames
 together and turning them into a video, you can embed files and folders of arbitrary size into videos and images.  
You're only limited by your hard drive.
+ **Variable block size:** Each of the blocks in the frame can be set to any size, including one pixel.  Larger block 
sizes give your stream protection in lossy environments, while smaller blocks allow for greater densities.

Currently, BitGlitter is configured to transport files and folders on a computer.  But with minimal modification you can
use videos or images as a carrier for virtually any kind of binary data.

### What this means in practical terms

Here's some real data that gives you an idea of what is possible with this:

Number of Colors | Bits Per Block | Screen Resolution | Block Size in Pixels | Block Dimensions | Framerate | Throughput | Lossless Application
--- | --- | --- | --- | --- | --- | --- | ---
2 | 1 | 640 x 480 (480p) | 20 | 32 x 24 | 30 | 2.88 KB/s | No
4 | 2 | 1280 × 720 (720p) | 20 | 64 x 36 | 30 | 17.28 KB/s | No
8 | 3 | 1280 × 720 (720p) | 20 | 64 x 36 | 30 | 25.92 KB/s | No
16 | 4 | 1920 x 1080 (1080p) | 20 | 96 x 54 | 30 | 77.76 KB/s | No
64 | 6 | 1920 x 1080 (1080p) | 20 | 96 x 54 | 30 | 116.64 KB/s | No
64 | 6 | 1920 x 1080 (1080p) | 20 | 96 x 54 | 60 | 233.28 KB/s | No
16,777,216 | 24 | 1920 x 1080 (1080p) | 5 | 384 x 216 | 30 | 7.47 MB/s | Yes
16,777,216 | 24 | 3840 x 2160 (4k) | 5 | 768 x 432 | 60 | 59.7 MB/s | Yes

Put simply, you can now make videos that can hold large amounts of data inside of them.  There may be some pretty
interesting applications that can come out of this.

# Features

### Data

+ **Supports streams up to ~1 EB in size, or ~4.3B frames:**  In other words, there is no practical limit to the
 stream's size.
+ **Compression added:** This is done automatically, so don't worry about putting your files in a rar or zip prior to
sending.
+ **Encryption added:** Optional AES-256 encryption to protect your files.  Passwords are hashed with `scrypt`, 
parameters can be customized for your needs.
+ **File masking:**  Optional ability to mask what files are included in the stream.  Only those who successfully grab 
the stream (and decrypt it if applicable) will know of its contents.

### Outputted Files

You can choose between either outputting all of your frames as a series of images (.png), or as a single .mp4.

+ **Customizable resolution:** You have complete control of the size of the outputted frames, whether they are 480p or
8K.
+ **Customizable framerate:** Currently supports 30 and 60 FPS, custom values are coming soon.

![Custom Color Showcase](https://i.imgur.com/4uQTxwT.png)

+ **Custom Color Palettes:** The included default palettes are just a starting point.  Make any color palette that you
want to match the aesthetic where it's being used.  Anyone reading the stream will have the palette automatically saved
to their machine, so then they can use it as well!  Functionality is included to output a text file outlining all of the
color palettes you have available to use, both default and custom.

### Reading

+ **Error correction against compression or corruption:** BitGlitter protects your file against corruption and artifacts 
on the image or video. After loading the correct palette, whenever it detects an incorrect color, it will "snap" it to 
the nearest color in the palette.  This gives your file resistance against format changes, codecs, or file size 
reduction.  This allows BitGlitter streams to still be read in environments that would otherwise render all existing 
steganography methods unreadable.

+ **Complete file integrity:** When the stream is created, a hash (SHA-256) is taken of the entire stream, as
well as each frame.  The data must match what is expected to be accepted.  Damaged or corrupt files will not be blindly
passed on to you.

+ **Streamlined frame bypassing:**  If a frame cannot or doesn't need to be read (ie, a duplicate already read), the 
reader determines this from an initial frame header

### Design

+ **No metadata saved in the file:**  Compress the stream, change formats, upload it somewhere.  All data is encoded in
the blocks, so you don't have to worry (as much) about rendering the stream unreadable.

+ **Easy to understand:** Whether you're learning about Python and want to understand how it works, or you're looking to
contribute, docstrings and notes are throughout the library.

+ **Built in future-proofing:** As of now, BitGlitter has a single protocol (Protocol 1), which is a specific set of
  procedures around how data is handled, and the components of a frame, as well as their layout.  Each protocol has its
  own unique ID to identify it with.  This ID is added in the  header during the write process, and is picked up at 
  `read()`.  As new protocols get created, older versions of BitGlitter that don't have these included will notify the user
  to update their version in order for it to be read.  All older protocol versions are saved in future library
  iterations, so no matter how old the protocol version is used on the stream, it will always be able to be read.

+ **Fully modular design:** Do you have a specialized use case?  Adapting this library to your own needs is quite easy.
  I've built BitGlitter to be easy to modify and expand upon.  Rather than worrying about the lower-level functionality,
  achieve your goal with the modular components I've created.


### Applications
To be determined.  This will be updated as time progresses!

# How to use

All of the functions to run this library are explained below.  I'm also working on several Wikipedia pages, explaining
BitGlitter in greater detail (how it works, etc) with some included illustrations.  These are not yet complete, 
[but here is the link to the project's Wiki if you'd like to see it!](https://github.com/MarkMichon1/BitGlitter/wiki/Using-BitGlitter)


**Third Party Libraries Used**

+ `bitstring` - Bit manipulation.
+ `cryptography` - Cryptographic functions.
+ `ffmpeg-python` - Video rendering and output.
+ `opencv-python` - Video loading and frame manipulation.
+ `Pillow` - Frame creation and output, as well as loading images and reading pixel values.
+ `PyQt5` - GUI framework.
+ `sqlalchemy` - Data persistence.

Thanks to Tanmay Mishra for giving me a pre-release version of his upcoming library `filepackager`.  It has been heavily
modified and stripped down to suit this library.  The code is included with BitGlitter; there is no need to download it.

**BitGlitter in 60 seconds**

`tba, many changes switching from library to GUI!`

### General Configuration

`tba`

# Contributing

Whether you're a seasoned programmer or brand new, there's plenty of things you can do to help this project succeed.
Join our discord server, and check out all of the information I posted in the "Information" category.  Thank you for
your interest!

**Discord Link**

**https://discord.gg/t9uv2pZ**

Also, be sure to check out the 
[contributing master page](https://github.com/MarkMichon1/BitGlitter/wiki/Contributing-Master-Page).  It contains a lot
of information.

![Splitter](https://i.imgur.com/qIygifj.png)

### Practical Limits

It's worth stating the constraints you may face while using this.  While the images and video BitGlitter exports are
lossless (no compression applied), the "real world" on the internet is much different.  For instance, multimedia 
uploaded to popular social media sites is regularly compressed in order to save space (and ultimately cut down on 
expenses).  You are protected *to an extent* with BitGlitter from this.  Write parameters are fully customizable
primarily for this reason.  

While you can have greater throughput with larger colorsets, smaller blocks, and faster framerates, there may be a
practical limit to whether it will work depending on the degree their compression reduces quality.  At the expense of
throughput, larger blocks, slower framerates, and fewer colors used will make the stream *far* more resistant to
possible corruption.  Approaching the extreme limits of these parameters (tiny block sizes, very fast framerates, very
large colorsets), in terms of reading it and converting it back into data, requires very precise measurements of
position and color value; *a codec's purpose is to blur those precise values to reduce it's bitrate, and in turn it's
file size.*  While BitGlitter will detect corruption and perform an "emergency stop," I know you don't want to deal with
that, and neither do the people you're sharing with.

In closing, know the environment the video will be used in to ensure success in reading it.

# MIT License
© 2019 - ∞ Mark Michon

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated 
documentation files (the "Software"), to deal in the Software without restriction, including without limitation the 
rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit
 persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the 
Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE 
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR 
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR 
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

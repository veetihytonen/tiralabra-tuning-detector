# Progress report of week 2

I had very limited time this week and unfortunately have not started working on the FFT algorithm yet. I have, at least, set up the project and dev tooling. I've also written a wrapper to handle reading WAV file content and turning it into a Numpy array. A fair bit of my time was spent researching what exactly it is that I'm reading out of a WAV file, and what I should do with it in order to prepare it for the FFT. I have decided to limit the file format to 16 bit 44.1kHz for now, but have made an effort to write the file reader wrapper in such a way that it is easy to implement support for an arbitrary format. 

I have not written any tests yet, as the wrapper is mainly just dealing with file I/O, and doesn't really contain any real work being done. Tests will come once I start writing the actual algorithm. 

Overall, a time constrained week for me, but I'm excited to dive into the project more deeply next week.

## Time spent

#### This week: 10h
#### Project total: 14h
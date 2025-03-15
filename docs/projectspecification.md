# Project specification

This is the specification document for the course Algorithms and AI lab, spring of 2025 for the bachelor's in computer science (CS) program.

## Description

The aim of the project is to implement an algorithm to detect the tuning of a piece of music, and alter the pitch of the piece such that it matches the tuning standard A=440Hz if it previously didn't. Tuning in this context refers to what frequency the A note above a middle C is tuned to, the standard in western music today being [A=440Hz](https://en.wikipedia.org/wiki/A440_(pitch_standard)). The inspiration for this project came from the frustration of trying to play along with a piece of music, only to realize it's not in standard tuning which makes my standard tuned instrument sound out of tune. This project solves that problem by "correcting" the tuning of a piece of music to standard.

There are two prominent algorithms, which are necessary for the project:

- Fast furier transform (FFT) to separate a piece of music into its constituent frequencies
- Phase vocoder to change the pitch of audio content while keeping relationship between notes intact

Needless to say, the core topic of the project is signal processing, and analysis of messy real world audio signals. 

Naturally, the decoding and encoding of audio files is necessary to do work on the signal and output a playable file. This is not in scope for the project and is consequently going to be handled with existing libraries. For the sake of simplicity, the program will only work with audio in WAV file format, as Python has a library for working with WAV files.

## Program usage

The program will be used via CLI. The user gives the name of an audio file as input for the program, and the program will create a new file containing a pitch corrected version of the original audio file. 

## Time complexity

The program will at best run in O(n log<sub>2</sub>(n)) time, as it is the time complexity of FFT.

## Programming languages

The project will be written in Python. I am also comfortable in reviewing code in Javascript, and C to some extent, if it is needed.

## Languages

All the source code, doc strings and documentation will be written in english.

## Limitations and challenges

The program assumes the input sample of music is using the [12-tone equal temperament system](https://en.wikipedia.org/wiki/12_equal_temperament) for tuning, as it is almost universal in western music tradition. The multitude of other tuning systems are, while interesting, scoped out due to limited time.

Another assumption is that the tuning stays consistent troughout the provided sample of music. While it is entirely possible to compose music with varying tuning, such endeavors are also out of scope for the project.

Additionally, the program will most likely work best with music that is somewhat orthodox in approach. That is to say, it should ideally have clear and distinguishable melodic and/or harmonic content, as this yields more easily interpreted results in spectral analysis of the audio signal.
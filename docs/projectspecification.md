# Project specification

This is the specification document for the course Algorithms and AI lab, spring of 2025 for the bachelor's in computer science (CS) program.


## Description

The aim of the project is to implement an algorithm to detect the tuning of a piece of music, and alter the pitch of the piece such that it matches the tuning standard A=440Hz if it previously didn't. Tuning in this context refers to what frequency the A note above a middle C is tuned to, the standard in western music today being [A=440Hz](https://en.wikipedia.org/wiki/A440_(pitch_standard)). The inspiration for this project came from the frustration of trying to play along with a piece of music, only to realize it's not in standard tuning which makes my standard tuned instrument sound out of tune. This project solves that problem by "correcting" the tuning of a piece of music to standard.

There are two prominent algorithms, which are necessary for the project:

- Fast furier transform to separate a piece of music into its constituent frequencies
- Phase vocoder to change the pitch of audio content while keeping relationship between notes intact

The project will use standard data structures, such as lists(arrays) and dictionaries (hash tables).

Needless to say, the core topic of the project is signal processing, and dealing with messy real world audio signals.

## Program usage

The program will be used via CLI. The user gives the name of an audio file as input for the program, and the program will create a new file containig a pitch corrected version of the original audio file.

## Time complexity

Program will at best run in O(n log(n)) time, as it is the time complexity of FFT

## Programming languages

The project will be written in Python. I am also comfortable in reviewing code in Javascript, and C to some extent, if it is needed.
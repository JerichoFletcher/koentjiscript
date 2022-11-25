# Parser Bahasa JavaScript

> Program yang memeriksa file javascript. Program ini dibuat sebagai pemenuhan Tugas Besar mata kuliah Teori Bahasa Formal dan Otomata IF2124

## Table Of Contents
* [General Information](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Screenshots](#screenshots)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#status-project)
* [Room for Improvement](#room-for-improvement)
* [Group Members](#group-members)
* [Program Structures](#program-structures)

## General Information
- Program ini adalah program yang menerima input sebuah file javascript dan memeriksa apakah syntax sudah valid atau tidak
- Program ini dibuat dengan memanfaatkan algoritma CYK (Cocke-Young-Kasami)

## Technologies Used
Python 3.9.6

## Features
Fitur dalam aplikasi ini adalah:
- Fitur parser javascript

## Setup
Prerequirement
- Python: https://www.python.org/downloads/

## Usage
`py koentjiscript.py <file javascript>`

## Status Project
Project is: currently worked on

## Room for Improvement


## Group Members

| NIM        | Names                                     | 
| -----------| ----------------------------------------- |
| 13521042   | Kevin John Wesley Hutabarat               |
| 13521051   | Manuella Ivana Uli Sianipar               |
| 13521107   | Jericho Russel Sebastian                  | 

## Program Structures
```
|-  README.md
|-  .gitignore
|- koentjiparse
|     |- parser.py
|     |- __init__.py
|- koentjiuti
|     |- __init__.py
|     |- cfg.py
|     |- cyk.py
|     |- dfa.py
|     |- expr.py
|     |- util_dict.py
|- __init__.py
|- cfg.txt
|- koentjiscript.py
|- test1.js

```


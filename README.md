# Kattis Problems

Repository with some of the [Kattis](https://open.kattis.com) problems solved.

## Python

### Conda Environmet

Anaconda prompt:

```
$ conda activate kattis
```

## Add Paths

```
$ add_paths.bat
```

## Create Problem

### Helper program

```
$ create_problem hello
```

## C

### Compile

```
$ gcc -Wall -g -O2 -std=gnu11 -static hello.c -lm -o hello.exe
```

### Helper program

```
$ create_c_exe hello
```

## C++

### Compile

```
$ g++ -Wall -g -O2 -std=gnu++17 -static hello.c -lm -o hello.exe
```

### Helper program

```
$ create_cpp_exe hello
```

## Test

### Helper program

```
$ test_problem hello.py
```

```
$ test_problem hello.exe
```

## Submit

### Helper program

```
$ submit hello.py
```

## LICENSE

The contents of this repository are covered under the [MIT License](LICENSE).

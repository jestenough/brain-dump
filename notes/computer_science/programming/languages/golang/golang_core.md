# Golang core

## Scope

The **case** of the **first letter** of a variable **determines** its **visibility** outside the project. If **name begins** with a **capital** letter **it is exportable**, i.e. _visible_ and _available_ from outside of the own package and the other parts of the program can access to the it, e.g. the _Printf_ fucntion from _fmt_ package.

### Lifetime of variables

The lifetime of the package level variable is equal to the running time of the entire program. The lifetime of local variables has a _dynamic lifetime_: a new instance is created each time the declaration statemenet is executed. The parametrs and result variables of the functions are _local variables._

- [ ] WRITE MORE ABOUT STACK/HEAP



## Types

Go is _a compiled programming language_ that is considered strongly and statically typed.

### Integers

|*Type*|*Range*|*Size*
|:----|:-----:|:----|
|`int8`|`-128 to 127`| **8 bits**|
|`uint8,byte`|`0 to 255`| **8 bits**|
|`int16`|`-32_768 to 32_767`|**16 bits**|
|`int32,rune,int,uintptr`|`-2_147_483_648 to 2_147_483_647`|**32 bits**|
|`uint, uint32`|`0 to 4_294_967_295`|**32 bits**|
|`int,int64`|`-9_223_372_036_854_775_808 to 9_223_372_036_854_775_807`|**64 bits**|
|`uint,uint64,uintptr`|`0 to 18_446_744_073_709_551_615`|**64 bits**|

> The `int`, `uint`, and `uintptr` types are usually **32 bits** wide **on 32-bit systems** and **64 bits** wide **on 64-bit systems**

Since integer types use two's complement arithmetic, you can infer the min/max constant values for `int` and `uint`. For example

```go
const MaxUint = ^uint(0)
const MinUint = 0
const MaxInt = int(MaxUint >> 1)
const MinInt = -MaxInt - 1
```

Type aliasing [example](https://github.com/golang/go/blob/4f1f503373cda7160392be94e3849b0c9b9ebbda/src/cmd/compile/internal/gc/universe.go#L409)


### Floats

|*Type*|*Range*|*Size*|*Precision*
|:-----|:-----:|:-----|:---------|
|`float32`|Approximately `±1.18e-38 to ±3.4e38`| **32 bits**|around **7** decimal digits|
|`float64`|Approximately `±2.23e-308 to ±1.80e308`|**64 bits**|around **15** decimal digits|

> When you don't set the type of a floating-point number, Golang will consider it as a `float64` type by **default**.

Floats goes to infinity when overflowed
```go
f := float32(math.MaxFloat32)
fmt.Println("max float: ", f*1.2) // max float: +Inf
```

### Complex

|*Type*|*Range*|
|:-----|:-----:|
`complex64`|set of all complex numbers with float32 real and imaginary parts|
`complex128`|set of all complex numbers with float64 real and imaginary parts|

> If you don't specify the type of a complex variable, it will be `complex128` by **default**.


## Links

[Go spec](https://go.dev/ref/spec)

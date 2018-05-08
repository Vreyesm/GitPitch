## Lenguajes y Paradigmas de Programación
### Scope estático y dinámico

<br>

Daniel Pavez - Victor Reyes

---
## Scope estático
---
### Código de ejemplo

```perl
$a = "global";
sub foo {
  return $a;
}
sub staticScope {
  my $a = "static";
  print $a . "\n";
  return foo();
}
print staticScope();
```
---
### ¿Cómo funciona?

Un binding estático ocurre antes del tiempo de ejecución y se mantiene sin cambios a lo largo de dicha ejecución.

```perl
$a = "global"; # Asignación $a = "global"
sub foo {
  return $a; # Asignación $a = "global"
}
sub staticScope {
  my $a = "static"; # Asignación $a = "static"
  print $a . "\n"; # $a de staticScope
  return foo();
}
print staticScope(); # $a de foo ("global")
```
@fa[arrow-down]

+++

#### Resultado
```
static
global
```
---
### Modifiquemos un poco nuestro programa
```perl
$a = "global";
sub foo {
  print $a . "\n"; # Modificación
  return $a;
}
sub staticScope {
  my $a = "static";
  print $a . "\n";
  return foo();
}
print staticScope();
```
@fa[arrow-down]

+++

#### Resultado
```
static
global
global
```
---
### Equivalencia
```perl
$a = "global";
sub foo {
  print $a . "\n";
  return $a;
}
sub staticScope {
  my $a = "static";
  print $a . "\n";
  return foo();
}
print staticScope();
```
@fa[arrow-down]

+++
```perl
$a = "global";
$a2 = "static"; # staticScope
print $a2 . "\n";
print $a . "\n";
print $a; # fuera
```
---
## Scope dinámico
---
### Código de ejemplo
```perl
$b = "global";
sub bar {
  return $b;
}
sub dynamicScope {
  local $b = "dynamic";
  print $b . "\n";
  return bar();
}
print dynamicScope();
```
---
### ¿Cómo funciona?

Un binding es dinámico si ocurre durante el tiempo de ejecución o puede cambiar en el transcurso de dicha ejecución.

```perl
$b = "global"; # Asignación de $b = "global"
sub bar {
  return $b; # Asignación de $b = "global"
}
sub dynamicScope {
  local $b = "dynamic"; # Asignación de $b = "dynamic"
  print $b . "\n";      # válido al interior de dynamicScope
  return bar(); # Pasa el valor de $b a la función bar
}
print dynamicScope();
```
@fa[arrow-down]

+++

#### Resultado

```
dynamic
dynamic
```
---
### Modifiquemos un poco nuestro programa
```perl
$b = "global";
sub bar {
  print $b . "\n" # Modificación
  return $b;
}
sub dynamicScope {
  local $b = "dynamic";
  print $b . "\n";
  return bar();
}
print dynamicScope();
```
@fa[arrow-down]

+++

#### Resultado

```
dynamic
dynamic
dynamic
```
---
### Equivalencia
```perl
$b = "global";
sub bar {
  print $b . "\n"
  return $b;
}
sub dynamicScope {
  local $b = "dynamic";
  print $b . "\n";
  return bar();
}
print dynamicScope();
```
@fa[arrow-down]

+++

```perl
$b = "global";
$b = "dynamic"; # dynamicScope
print $b . "\n";
print $b . "\n"; # bar
print $b; # fuera
```
---
### Modifiquemos un poco nuestro programa (nuevamente)
```perl
$b = "global";
sub bar {
  print $b . "\n"
  return $b;
}
sub dynamicScope {
  local $b = "dynamic";
  print $b . "\n";
  return bar();
}
print dynamicScope() . "\n";
print $b; # Modificación (static)
```
@fa[arrow-down]

+++

#### Resultado

```
dynamic
dynamic
dynamic
global
```
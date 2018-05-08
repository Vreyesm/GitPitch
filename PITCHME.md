## Lenguajes y Paradigmas de Programación
### Flujo de Control

<br>

Daniel Pavez - Victor Reyes

---
### ¿Qué es el Flujo de Control?

Es el orden que sigue la ejecución de un programa, con el fin de cumplir la tarea deseada.

---

### Categorías de mecanismos utilizados

@ol

- *Secuenciamiento:* El orden en que se ejecutan las sentencias o se evaluan las expresiones (usualmente en el orden en que aparecen en el código del programa).
- *Selección:* Dependiendo de alguna condición en tiempo de ejecución, se realiza una elección entre dos sentencias o expresiones. Los casos más comunes son las sentencias `if` y `case (switch)`.

@olend

@fa[arrow-down]

+++

@ol

- *Iteración:* Ejecución repetitiva de un cierto fragmento de código, ya sea un cierto número de veces o hasta que una condición (en tiempo de ejecución) sea verdadera. Incluyen las sentencias `for`, `while` y `repeat`.
- *Abstracción procedural:* Un conjunto de constructos potencialmente complejos (una subrutina) son encapsulados, con el fin de ser tratados como única unidad, usualmente sujeta a la parametrización.

@olend

@fa[arrow-down]

+++

- *Recursión:* Una expresión ques es definida en terminos (versiones más simples) de sí misma, ya sea directa o indirectamente. Para ello, el modelo computacional requiere un "stack" o "pila" para almacenar la información sobre las instancias parcialmente evaluadas de la expresión. Comunmente, es utilizada por medio de subrutinas que se autoreferencian.

@fa[arrow-down]

+++
- *Concurrencia*: Dos o más fragmentos de un programa que son ejecutados/evaluados "al mismo tiempo", ya sea en paralelo utilizando procesadores separados o intercalados en un único procesado, con el fin de conseguir el mismo efecto.

@fa[arrow-down]

+++

- *Manejo de excepciones y especulación:* Un fragmento de programa es ejecutado de manera optimista, asumiendo que una condición esperada se cumplirá. Si dicha condición no se cumple, la ejecución se ramifica a un "handler" que se ejecuta en lugar del resto del código protegido (en el caso del manejo de excepciones), o en lugar de todo el bloque de código protegido (en el caso de la especulación). Para la especulación, la implementación del lenguaje debe ser capaz de deshacer o retroceder cualquier efecto visible del código protegido.

@fa[arrow-down]

+++
- *Indeterminación:* El orden o elección de las sentencias o expresiones se dejan deliberadamente sin especificar, dando a entender que cualquier alternativa llevará a un resutlado correcto. Algunos lenguajes requieren que la elección de aleatoria o pareja, en el sentido formal de la palabra.

---
## Evaluación de expresiones
---
@fa[arrow-down]

+++
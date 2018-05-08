## Lenguajes y Paradigmas de Programación
### Flujo de Control

<br>

Daniel Pavez - Victor Reyes

---
### ¿Qué es el Flujo de Control?

Es el orden que sigue la ejecución de un programa, con el fin de cumplir la tarea deseada.

---

### Categorías de mecanismos utilizados

@ul

- **Secuenciamiento:** El orden en que se ejecutan las sentencias o se evalúan las expresiones (usualmente en el orden en que aparecen en el código del programa).

- **Selección:** Dependiendo de alguna condición en tiempo de ejecución, se realiza una elección entre dos sentencias o expresiones. Los casos más comunes son las sentencias `if` y `case (switch)`.

@ulend

@fa[arrow-down]

+++

@ul

- **Iteración:** Ejecución repetitiva de un cierto fragmento de código, ya sea un cierto número de veces o hasta que una condición (en tiempo de ejecución) sea verdadera. Incluyen las sentencias `for`, `while` y `repeat`.
 
- **Abstracción procedural:** Un conjunto de constructos potencialmente complejos (una subrutina) son encapsulados, con el fin de ser tratados como única unidad, usualmente sujeta a la parametrización.

@ulend

@fa[arrow-down]

+++

- **Recursión:** Una expresión que es definida en términos (versiones más simples) de sí misma, ya sea directa o indirectamente. Para ello, el modelo computacional requiere un "stack" o "pila" para almacenar la información sobre las instancias parcialmente evaluadas de la expresión. Comúnmente, es utilizada por medio de subrutinas que se autoreferencian.

@fa[arrow-down]

+++

- **Concurrencia**: Dos o más fragmentos de un programa que son ejecutados/evaluados "al mismo tiempo", ya sea en paralelo utilizando procesadores separados o intercalados en un único procesado, con el fin de conseguir el mismo efecto.

@fa[arrow-down]

+++

- **Manejo de excepciones y especulación:** Un fragmento de programa es ejecutado de manera optimista, asumiendo que una condición esperada se cumplirá. Si dicha condición no se cumple, la ejecución se ramifica a un "handler" que se ejecuta en lugar del resto del código protegido (en el caso del manejo de excepciones), o en lugar de todo el bloque de código protegido (en el caso de la especulación). Para la especulación, la implementación del lenguaje debe ser capaz de deshacer o retroceder cualquier efecto visible del código protegido.

@fa[arrow-down]

+++

- **Indeterminación:** El orden o elección de las sentencias o expresiones se dejan deliberadamente sin especificar, dando a entender que cualquier alternativa llevará a un resultado correcto. Algunos lenguajes requieren que la elección de aleatoria o pareja, en el sentido formal de la palabra.

---
## Evaluación de expresiones
---

### Operadores


<ul align="left">
  <li class="fragment">
    <strong>Prefijos:</strong>
    <ul>
      <li><em>op</em> a b</li>
      <li><em>op</em> (a, b)</li>
      <li>(<em>op</em> a b)</li>
    </ul>
  </li>
  <li class="fragment">
    <strong>Infijos:</strong>
    <ul>
      <li>a <em>op</em> b</li>
    </ul>
  </li>
  <li class="fragment">
    <strong>Sufijos:</strong>
    <ul>
      <li>a b <em>op</em></li>
    </ul>
  </li>
</ul>
---

### Precedencia y asociatividad

@ul

- **Precedencia:** En ausencia de paréntesis, especifica el orden en son agrupadas las operaciones, siendo las de mayor precedencia las primeras en se agrupadas.

- **Asociatividad:** Especifica si una secuencia de operadores de la misma precedencia son agrupados hacia la izquierda o hacia la derecha.


- *Importantes cuando se utilizan operadores infijos.*
- *Cada lenguaje tiene su propia definición para la precedencia y asociatividad de sus operadores.*
- *Si no está seguro, haga uso de paréntesis.*

@ulend

@fa[arrow-down]

+++

![Image-Absolute](assets/Precedencia.png)
# ¿Por que aprender POO?

La programacion orientada a objetos nos ayuda a entender mejor nuestro codigo.

Ademas, como programador puede ser un punto de inflexion dentro de tu carrera para dejar de ser un **Programador Jr.** Y empezar a ser un **programador Sr.**

Dejaras de copiar codigo, y evitaras crear pequeños Frankenstein.

¿Como lo haremos?

1. Primero analizaremos nuestros problemas.
    - observando
    - entendiendo
    - leyendo
2. Plasmaremos nuestro analisis en diagramas.
3. Y por ultimo, empezaremos a programar.

## Que resuelve el POO?

La programacion orientada a objetos ayuda a resolver muchos de los problemas que la programacion estructurada no pudo.

- Evita el codigo muy largo.
    Antes habia personas que cobraban por linea de codigo, y llegaban a existir programas con 4000 lineas de codigo, lo que lo hacia dificil de sostener y entender.
- Si algo falla, todo se rompe.
    Si hay un pequeño error, todo despues de esa linea ya no seguiria ejecutandose.
- Dificil de mantener.
    Teniendo muchas lineas o problemas, era problematico de mantener.

El codigo espaghetti 
![Imagen codigo spaghetti](https://static.platzi.com/media/user_upload/Screen%20Shot%202020-03-15%20at%2011.44.20%20AM-6e2ae84d-dc98-4647-9c13-dbf69808785a.jpg)

## Paradigma del POO

La programacion orientada a objetos no solo resuelve problemas de la programacion estructurada.

La programacion orientada objetos **POO ** o **OOP**(**Oriented Object Programing** por sus siglas en ingles), proviene de un paradigma de **orientacion a objetos**.

La orientacion a objetos, surge a partir de problemas que tenemos y necesitamos plasmar en codigo, observandolos en forma de objetos.

Entonces la orientacion a objetos es un paradigma de POO.

Este paradigma contiene 4 pilares: Clases, Propiedades, metodos y Objetos.

Tambien tenemos encapsulamiento, Abstraccion, Herencia y Polimorfismo.

## Algunos lenguajes para POO/OOP

1. Java
    - Orientado a objetos naturalmente
    - Android.
    - Server Side
2. PHP
    - Lenguaje interpretado.
    - Orientado a objetos.
    - Pensado para la Web.
3. Python
    - Diseñado para ser facil de usar.
    - Hermoso.
    - Multiples usos: Web, Server Side, Analisis de Datos, Machine Learning, etc
    - Oriented Object Programing.
4. JavaScript
    - Lenguaje interpretado
    - Oriented Object pero basado en prototipos.
    - Pensado para la web.
    
## UML: Lenguaje de modelado unificado.

Es un lenguaje que toma las bases de OMT(**Object Modeling Techniques**) unificandolas y nos brinda más opciones como son las clases, Casos de uso, objetos, actividades, iteración, estados e implementación.

OMT nacio en 1991, y al ser UML un derivado con las mejores prácticas y mejoras de OMT, surge en 1998

## Objetos.

Todo proviene de objetos, y la programación orienada a objetos resuelve problemas modelandolos para luego modelarlos en código.

Lo primero que debemos hacer es **identificar los objetos**.

Y para  hacer esto, debemos tomar en cuenta que **Los objetos son aquellos que tienen propiedades y comportamientos**, además los objetos siempre seran **sustantivos**(*Palabra que sirve para designar los seres vivos o las cosas materiales o mentales*).

Pueden ser *físicos* o *conceptuales*.
![User vs Session](https://static.platzi.com/media/user_upload/Captura-1dc6b074-71d4-44a9-8d7a-4d631a44b904.jpg)

Las propiedades también pueden llamarse **atributos**, serán sustantivos.

Los **comportamientos** seran todas las operaciones del objeto, suelen ser verbos o sustantivo y verbo.

### Modularidad

Modular código es un método que divide el código en partes independientes entre si, y que además no tengan problemas para acoplarse luego entre ellas.

Esto ahorra problemas de código, sí alguna parte del programa se rompe, de ahora en adelante solo afectara al módulo donde se encuentre, y el código entero no colapsara.

- sera legible
- Reutilizable
- Evitara códigos largos y complejos
- Permitira separar nuestro código
- Se resolveran más rapido y facil los problemas
- Además de ser mantenible.

### Escribiendo clases y objetos con POO.

![Class person](https://static.platzi.com/media/user_upload/Captura-8a63bd95-1961-4745-b192-9421b0bc24b5.jpg)

Podemos escribir los atributos y comportamientos en python:

```py
Class Person:
    name: str = ""
    def walk():
        ...
```

``` Java
class Person {
	String name = "";
	void walk(){ }
}
```

``` Js
Person.prototype.walk = function(){

}
```

``` Php
class Person {
    $name = "";
    function walk(){}
}
```

```js
"Con EcmaScript6 Ya podemos usar class en JS"
class Rectangulo {
  constructor(alto, ancho) {
    this.alto = alto;
    this.ancho = ancho;
  }
}
La palabra reservada para ello es Class
```

## DRY: Don't repeat your self.

- Evitaremos duplicar líneas de código en nuestro código.
- Toda pieza de información **Nunca debería ser duplicada** porque esto **aumenta la dificultad** en los cambios y evolución del código.

Entonces: **Reutilizaremos código.**

Para reutilizar necesitamos la **Herencia**, que nos permite *crear nuevas clases a partir de otras*.

La Herencia, establece un **Padre, e hijo/s**.
- Padre: nos referimos a esta clase como *Superclase*.
- Hija: a esta clase le llamaremos *subclase*.

Cuando una clase Padre(*superclase*) tiene atributos y comportamientos, esto significa que todas las clases hijas(*subclases*) los heredaran aunque no quede reflejado en el código.

En algunas situaciones, que no compartan elementos, la lógica de negocio podría necesitar que unamos estos objetos en una clase más general, que también puede llamarse *superclase*.

![Captura_comentario.PNG](https://static.platzi.com/media/user_upload/Captura_comentario-32b17ace-f3dc-44ac-a057-eeed46425bdd.jpg)

Te comparto notas donde muestra flechas de relación en UML. Segmento diagramas de Modelado.
[Notas de @AndresSantiste9](https://docs.google.com/document/d/1xdJFOeKRVMoZqtl-cTigUKX-oSElnstW0T6qlDRbiSE/edit)

El ejemplo de nuetra tienda de mascotas: 
![petsStoreExample](https://static.platzi.com/media/user_upload/Untitled%20Diagram%20%281%29-aaeda0b3-dc41-439a-bc78-951660c64edd.jpg)

Perfecto, ya habiendo modelado nuestro refugio de mascotas en UML, podemos ir a la parte que todos esperamos, **el código.**

Objetos, método constructor y su sintaxis en códigoen Java, Python, JavaScript y PHP.

Un objeto es una **instancia** de la clase. Es decir, el objeto es el resultado de lo que modelamos o los parámetros que dejamos declarados en la clase.

```Java
Person juan = new Person();
```
```Python
persona = Person()
```
JavaScript
```JavaScript
const person = new Person();
```
PHP
```PHP
$person = new Person();
```
Ruby
```Ruby
persona = Person.new()
```
Los Paréntesis en OPP representan métodos. Y estos métodos se escriben en mayúscula y tienen el mismo nombre de la clase, a estos se les llama **método constructor**.

El **método constructor** se encarga de dar un estado inicial al objeto. Le da una vida en memoria. Además podemos añadirles los datos al objeto a través del método constructor.

De hecho, los datos que le pasaremos a través del constructor serán los datos mínimos que necesita el objeto para que pueda vivir.

Para crear este método constructor lo hacemos:

Java
```Java
public Person(String name){
   this.name = name;
}
```
Python
```Python
def __init__(self,name):
    self.name = name
```
JavaScript
```JavaScript
// A partir de ES6 el constructor se hace dentro de class, así:
class Square {
  // Este es el construtor
  constructor(length) {
    this.name = 'Square';
  }
}
```
PHP
```PHP
public function __construct($name) {
    $this->name = name;
}
```
Ruby
```Ruby
class Person
  attr_reader :name
  
  # Aquí esta el constructor
  def initialize(name)
    @name = name
  end
end
```
**C#**
![EnC#.PNG](https://static.platzi.com/media/user_upload/Captura-90a2bd64-4742-47bb-84e5-de152bb731cb.jpg)
# Tesis
En este repositorio se encuentran los programas utilizados en la Tesis de licenciatura

El codigo de vacantes encuentra la política óptima del siguiente problema:

Un reclutador es contratado por una empresa, donde hay N tipos de puestos disponibles, cada vez que se entrevista a un candidato, 
independientemente de los entrevistados con anterioridad, aplicará para el puesto i con probabilidad Pi para i = 1, . . . , N. 
En cada etapa la empresa puede decidir pagar un costo C al reclutador,
al cual solo le es posible entrevistar a lo más a un candidato en dicha etapa, o decidir
no hacerlo. Si decide pagar el costo, puede llegar un candidato en busca de empleo
con probabilidad α, si decide no continuar pagando al reclutador la empresa recibe
la recompensa terminal R(n) generada por los n tipos de puestos cubiertos.

El código de inventario encuentra la política óptima del siguiente problema:

Considérese Xt el stock de un inventario al tiempo t, el cual sigue la
dinámica, At denota la cantidad
pedida al principio del periodo t.

Xt+1 = (Xt + At − ξt+1)+,

donde ξt representa la demanda en el periodo t.
Se considera que el almacén tiene una capacidad
finita M ∈ Z+, de esta manera, el espacio de estados es X = {0, 1, 2, . . . , M }, si la
demanda excede la cantidad de producto existente, se paga una penalización y no hay
pedidos pendientes.
Se establece:

h ≡ Costo de almacenaje por unidad.

p ≡ Costo de penalización (deuda de producto)
b ≡ costo de producción

En este caso se considera la siguiente función de costo:

C(Xt, At, ξt) = bAt + h m ́ax{0, Xt + At − ξt+1} + p m ́ax{0, −Xt − At + ξt+1}

Se requiere el costo total esperado para 6 etapas,la distribución de la
demanda está dada en la siguiente tabla

k  0  1   2   3   4   5

pk 0 0.1 0.1 0.3 0.3 0.2

A(x) = {0, 1, . . . , 5 − x} ∀x ∈ X,
donde X representa el espacio de estados, en este ejemplo se tomará h = 2 y p = 10.
se toma N = 6, el costo terminal, cN (x) = 0, ∀x ∈ X
y b = 5, de esta manera, se desea calcular el inimo costo total esperado del tiempo t al tiempo N.

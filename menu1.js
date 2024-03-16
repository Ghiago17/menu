let opcion = prompt("Selecciona una opción:\n1. Personas\n2. Vehiculos\n3. Universidades\n4. Notas\n5. Salir");

switch(opcion) {
    case '1':
        console.log("Hola, has presionado la opción Personas");
        break;
    case '2':
        console.log("Hola, has presionado la opción Vehiculos");
        break;
    case '3':
        console.log("Hola, has presionado la opción Universidades");
        break;
    case '4':
        console.log("Hola, has presionado la opción Notas");
        break;
    case '5':
        console.log("Has seleccionado Salir, el programa finalizará.");
        break;
    default:
        console.log("Opción no válida");
}

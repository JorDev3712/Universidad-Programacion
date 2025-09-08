import persona.Persona;

class MainPruebaPersona {
    public static void main(String[] args) {
        // We make the class
        System.out.println("*** Class Creation and persona.Persona Objects ***");
        Persona person = new Persona("Jor", "Vas");
        person.showPerson();
    }
}
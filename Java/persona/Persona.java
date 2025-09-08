package persona;

public class Persona {
    private String name;
    private String lastname;

    public Persona(String name, String lastname){
        this.name = name;
        this.lastname = lastname;
    }

    public String getName() {
        return this.name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getLastname() {
        return this.lastname;
    }

    public void setLastname(String lastname) {
        this.lastname = lastname;
    }

    public void showPerson() {
        System.out.println(String.format("La persona se llama %s %s", this.getName(), this.getLastname()));
    }
}

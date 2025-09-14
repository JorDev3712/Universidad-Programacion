package proyecto_maquina_snacks.v2.services;

import java.util.List;

import proyecto_maquina_snacks.v2.dominion.Snack;

public interface IServicioSnacks {
    Snack getSnack(Integer id);
    void initialize();
    void addSnack(String name, Double cost);
    void showSnacks();

    List<Snack> getSnacks();
}

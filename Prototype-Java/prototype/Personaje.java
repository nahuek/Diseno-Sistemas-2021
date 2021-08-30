package prototype;

public abstract class Personaje implements PersonajeClonable{

    public int vida;
    public int ataque;

    public Personaje(int vida, int ataque){
        this.vida = vida;
        this.ataque = ataque;
    }

    @Override
    public abstract PersonajeClonable clone();
}

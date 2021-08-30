package prototype;

public class Duende extends Personaje{
    
    public static final int VIDA = 200;
    public static final int ATAQUE = 150;

    public Duende(){
        super(VIDA, ATAQUE);
    }

    @Override
    public PersonajeClonable clone(){
        Duende clon = new Duende();
        clon.vida = this.vida;
        clon.ataque = this.ataque;
        return clon;
    }
    public String toString(){
        return "duende";
    }
}

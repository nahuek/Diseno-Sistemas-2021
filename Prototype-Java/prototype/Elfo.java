package prototype;

public class Elfo extends Personaje{
    
    public static final int VIDA = 100;
    public static final int ATAQUE = 250;

    public Elfo(){
        super(VIDA, ATAQUE);
    }

    @Override
    public PersonajeClonable clone(){
        Elfo clon = new Elfo();
        clon.vida = this.vida;
        clon.ataque = this.ataque;
        return clon;
    }
    public String toString(){
        return "elfo";
    }
}

package prototype;

public class Orco extends Personaje{
    
    public static final int VIDA = 20;
    public static final int ATAQUE = 700;

    public Orco(){
        super(VIDA, ATAQUE);
    }

    @Override
    public PersonajeClonable clone(){
        Orco clon = new Orco();
        clon.vida = this.vida;
        clon.ataque = this.ataque;
        return clon;
    }
    public String toString(){
        return "orco";
    }
}

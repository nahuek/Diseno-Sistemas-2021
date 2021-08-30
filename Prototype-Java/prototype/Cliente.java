package prototype;

public class Cliente {

    public static void main(String[] args){
        Personaje[] personajes = new Personaje[3];
        personajes[0] = new Elfo();
        personajes[1] = new Orco();
        personajes[2] = new Duende();

        for(Personaje p: personajes){
            System.out.println("Creado " + p.toString() + "s...");
            for(int i = 0; i < 3; i++){
                System.out.println("Soy un " + p.clone());
            }
        }
    }
    
}

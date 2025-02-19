import java.util.ArrayList;

interface MyDatastructure<T> {
    void addElement(T data);
    T removeElement();
    void printAll();
}

interface Printable {
    void printInAFunnyWay();
}


class Stack<T> implements MyDatastructure<T>, Printable {

    private ArrayList<T> elements;

    public Stack() {
        elements = new ArrayList<T>();
    }

    public void addElement(T data) {
        this.elements.add(data);
    }

    public T removeElement() {
        if (this.elements.isEmpty()) {
            return null;
        }
        T toRemove = elements.get(elements.size()-1);
        elements.remove(elements.size()-1);
        return toRemove;
    }

    public void printAll() {
        for (T s : this.elements) {
            System.out.println(s);
        }
    }

    public void printInAFunnyWay() {
        for (T s: this.elements) {
            System.out.println("Skibidi " + s);
        }
    }
}

class Studentsystem {

    public Studentsystem() {

    }

    public void leggTilStudent(String navn) {

    }

    public String fjernSisteStudent() {
        return null;
    }

    public void printAlleStudenter() {

    }
}

class Main {
    public static void main(String[] args) {
        Stack<Integer> s = new Stack<Integer>();
        s.addElement(1);
        s.addElement(2);

        s.printAll();
        s.printInAFunnyWay();
    }
}

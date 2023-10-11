package cw_02_toy_store_java.exceptions;

public class NullInput extends RuntimeException{
    public NullInput() {
        super("Некорректный ввод, строка не может быть пустой");
    }
}

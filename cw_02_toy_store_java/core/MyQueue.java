package cw_02_toy_store_java.core;

import java.io.FileWriter;
import java.io.IOException;
import java.util.PriorityQueue;
import java.util.Random;

public class MyQueue {

    public int get(PriorityQueue<Toy> queue) {
        int totalFrequency = 0;
        for (Toy toy : queue) {
            totalFrequency += toy.getFrequency();
        }

        Random random = new Random();
        int randomNumber = random.nextInt(totalFrequency) + 1;

        int currentFrequency = 0;
        for (Toy toy : queue) {
            currentFrequency += toy.getFrequency();
            if (randomNumber <= currentFrequency) {
                return toy.getId();
            }
        }

        return -1; // В случае ошибки
    }

    public void getQueue(PriorityQueue<Toy> queue) {
        try {
            FileWriter writer = new FileWriter("output.txt");

            // Вызов метода get 10 раз и запись результата в файл
            for (int i = 0; i < 10; i++) {
                int toyId = get(queue);
                writer.write(Integer.toString(toyId) + "\n");
            }

            writer.close();
            System.out.println("Данные успешно сохранены.");
        } catch (IOException e) {
            System.out.println("Произошла ошибка записи в файл.");
            e.printStackTrace();
        }
    }
}

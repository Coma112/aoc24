import java.io.*;
import java.util.*;
import java.util.concurrent.atomic.AtomicInteger;

@SuppressWarnings("all")
public class Second {
    private static List<Integer> leftList = new ArrayList<>();
    private static List<Integer> rightList = new ArrayList<>();

    public static void main(String[] args) {
        try (BufferedReader reader = new BufferedReader(new FileReader("src/input.txt"))) {
            String line;

            while ((line = reader.readLine()) != null) {
                if (line.trim().isEmpty()) continue;


                String[] parts = line.trim().split("\\s+");

                if (parts.length == 2) {
                    try {
                        int left = Integer.parseInt(parts[0]);
                        int right = Integer.parseInt(parts[1]);

                        leftList.add(left);
                        rightList.add(right);
                    } catch (NumberFormatException exception) {
                        exception.printStackTrace();
                    }
                }
            }

            Map<Integer, Integer> rightCounts = new HashMap<>();

            rightList.forEach(num -> {
                rightCounts.put(num, rightCounts.getOrDefault(num, 0) + 1);
            });

            AtomicInteger totalSum = new AtomicInteger();

            leftList.forEach(num -> {
               totalSum.addAndGet(num * rightCounts.getOrDefault(num, 0));
            });

            System.out.println(totalSum.get());
        } catch (IOException exception) {
            exception.printStackTrace();
        }
    }
}
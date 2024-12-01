import java.io.*;
import java.util.*;

@SuppressWarnings("all")
public class First {
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

            Collections.sort(leftList);
            Collections.sort(rightList);

            int totalDifference = 0;

            for (int i = 0; i < leftList.size(); i++) {
                totalDifference += Math.abs(leftList.get(i) - rightList.get(i));
            }

            System.out.println(totalDifference);
        } catch (IOException exception) {
            exception.printStackTrace();
        }
    }
}
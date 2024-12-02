import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

@SuppressWarnings("all")
public class First {
    private static int safeCount = 0;
    private static List<Integer> numbers = new ArrayList<>();

    public static void main(String[] args) {
        try {
            List<String> lines = Files.readAllLines(Paths.get("src/input.txt"));

            lines.forEach(line -> {
                if (isSafe(line)) safeCount++;
            });

            System.out.println(safeCount);
        } catch (IOException exception) {
            exception.printStackTrace();
        }
    }

    private static boolean isSafe(String line) {
        String[] levelArray = line.split(" ");
        int[] numberArray = new int[levelArray.length];

        for (int i = 0; i < levelArray.length; i++) {
            numberArray[i] = Integer.parseInt(levelArray[i]);
        }

        for (int i = 1; i < numberArray.length; i++) {
            int difference = Math.abs(numberArray[i] - numberArray[i - 1]);

            if (difference < 1 || difference > 3) return false;
        }

        boolean increasing = true;
        boolean decreasing = true;

        for (int i = 0; i < numberArray.length - 1; i++) {
            if (numberArray[i] > numberArray[i + 1]) decreasing = false;
            else if (numberArray[i] < numberArray[i + 1]) increasing = false;
        }

        return increasing || decreasing;
    }
}
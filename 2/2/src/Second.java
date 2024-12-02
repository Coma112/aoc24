import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

@SuppressWarnings("all")
public class Second {
    private static int safeCount = 0;

    public static void main(String[] args) {
        try {
            List<String> lines = Files.readAllLines(Paths.get("src/input.txt"));

            lines.forEach(line -> {
                if (isSafe(line)) safeCount++;
                else if (canBeMadeSafe(line)) safeCount++;
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

        boolean increasing = true;
        boolean decreasing = true;

        for (int i = 0; i < numberArray.length - 1; i++) {
            int difference = Math.abs(numberArray[i] - numberArray[i + 1]);

            if (difference < 1 || difference > 3) return false;
            if (numberArray[i] < numberArray[i + 1]) decreasing = false;
            else if (numberArray[i] > numberArray[i + 1]) increasing = false;
        }

        return increasing || decreasing;
    }

    private static boolean canBeMadeSafe(String levels) {
        String[] levelArray = levels.split(" ");
        List<Integer> levelList = new ArrayList<>();

        for (String level : levelArray) {
            levelList.add(Integer.parseInt(level));
        }

        for (int i = 0; i < levelList.size(); i++) {
            List<Integer> newLevels = new ArrayList<>(levelList);

            newLevels.remove(i);

            if (isSafe(newLevelsToString(newLevels))) return true;
        }
        return false;
    }

    private static String newLevelsToString(List<Integer> levels) {
        StringBuilder stringBuilder = new StringBuilder();

        levels.forEach(level -> {
            stringBuilder
                    .append(level)
                    .append(" ");
        });

        return stringBuilder
                .toString()
                .trim();
    }
}
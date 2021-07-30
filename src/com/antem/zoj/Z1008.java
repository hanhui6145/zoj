package com.antem.zoj;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Z1008 {
//    public static void main(String[] args) {
//        int gameIndex = 1;
//
//        List<String> list = new ArrayList();
//        list.add(0, "68542");
//        list.add(1, "59140");
//        list.add(2, "44561");
//        list.add(3, "04433");
//        list.add(4, "68542");
//        list.add(5, "59140");
//        list.add(6, "44561");
//        list.add(7, "04433");
//        list.add(8, "04433");
//        if (hasResult(3, list)) {
//            System.out.println("Game " + gameIndex + ": Possible");
//        } else {
//            System.out.println("Game " + gameIndex + ": Impossible");
//        };
//        gameIndex++;
//    }
public static void main(String[] args) {
    int gameIndex = 1;
    Scanner in = new Scanner(System.in);
    while (in.hasNext()) {
        int n = in.nextInt();
        if (n == 0) {
            return;
        }
        List<String> list = new ArrayList();
        String nums = "";
        int times = 0;
        while (in.hasNext()) {
            nums += (in.nextInt());
            if (nums.length() == 4) {
                if (!list.contains(nums)) {
                    list.add(nums);
                }
                times++;
                nums = "";
            }
            if (times == n * n) {
                break;
            }
        }
        if (hasResult(n, list)) {
            System.out.println("Game " + gameIndex + ": Possible");
        } else {
            System.out.println("Game " + gameIndex + ": Impossible");
        };
        list.clear();
        gameIndex++;
        System.gc();
    }
}

    private static boolean hasResult(int n, List<String> list) {
        if (n == 1 || list.size() == 1) {
            return true;
        }
        List<List<String>> que = new ArrayList();
        for (int i = 0; i < list.size(); i++) {
            String item = list.get(i);
            list.set(i, item + i);
            List<String> qItem = new ArrayList();
            qItem.add(item + i);
            que.add(qItem);
        }
        do {
            List<String> qItem = que.get(que.size() - 1);
            que.remove(qItem);

            qItem.get(qItem.size() - 1);
            for (int i = 0; i < list.size(); i++) {
                String item = list.get(i);
                if (!isCanAdd(qItem, item, n)) {
                    char[] c = item.toCharArray();
                    if (c[0] == c[1] && c[1] == c[2] && c[2] == c[3]) {
                        qItem.clear();
                        que.clear();
                        return false;
                    }
                    continue;
                }
                List<String> map = new ArrayList(qItem);
                map.add(item);
                if (map.size() == list.size()) {
                    qItem.clear();
                    que.clear();
                    return true;
                }
                que.add(map);
            }
            qItem.clear();
        } while (que.size() > 0);
        return false;
    }

    private static boolean isCanAdd(List<String> qItem, String addQue, int n) {
        int size = qItem.size();
        int addLine = (int)Math.ceil((float) size / (float)n);
        int lastCol = size % n;
        boolean result = true;
        if (addLine != 1) {
            String addQueTop = qItem.get((addLine - 2) * n + lastCol);
            result = addQueTop.substring(2, 3).equals(addQue.substring(0, 1));
        }
        if (lastCol != 0 && result) {
            String addQueLeft = qItem.get((addLine - 1) * n + lastCol - 1);
            result = result && addQueLeft.substring(1, 2).equals(addQue.substring(3, 4));
        }
        if (result) {
            for (String q : qItem) {
                if (q.substring(4, 5).equals(addQue.substring(4))) {
                    return false;
                }
            }
        }
        return result;
    }
}
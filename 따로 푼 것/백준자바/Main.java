// 이중 우선 순위 큐

import java.io.*;
import java.util.StringTokenizer;

class DLink {
    private int item;
    private DLink next;
    private DLink prev;

    DLink(int item, DLink prev, DLink next) {
        this.item = item;
        this.prev = prev;
        this.next = next;
    }

    DLink next() {
        return next;
    }

    DLink setNext(DLink next) {
        return this.next = next;
    }

    DLink prev() {
        return prev;
    }

    DLink setPrev(DLink prev) {
        return this.prev = prev;
    }

    int item() {
        return item;
    }

    int setItem(int item) {
        return this.item = item;
    }
}

class DList {
    DLink head, tail;
    int size;

    public DList() {
        head = new DLink(-2147483648, null, tail);
        tail = new DLink(2147483647, head, null);
        size = 0;
    }

    public void insert(int item) {
        DLink curr = head;
        while (item > curr.next().item()) {
            curr = curr.next();
        }
        curr.setNext(new DLink(item, curr, curr.next()));
        curr.next().next().setPrev(curr.next());
        size++;
    }

    public void clear() {
        head.setNext(tail);
        tail.setPrev(head);
        size = 0;
    }

    public void deF() {
        if (size > 0) {
            head.setNext(head.next().next());
            head.next().setPrev(head);
            size--;
        }
    }

    public void deB() {
        if (size > 0) {
            tail.setPrev(tail.prev().prev());
            tail.prev().setNext(tail);
            size--;
        }
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        DList DDL = new DList();
        for (int i = 0; i < T; i++) {
            DDL.clear();
            int e = Integer.parseInt(br.readLine());

            for (int j=0; j<e;j++){
                StringTokenizer st = new StringTokenizer(br.readLine());
                char c = st.nextToken().charAt(0);
                int r = Integer.parseInt(st.nextToken());
                if (c == 'I') {
                    DDL.insert(r);
                }
                else {
                    if (r==1) DDL.deB();
                    else DDL.deF();
                }
            }
            if (DDL.size == 0) System.out.println("EMPTY");
            else System.out.println(DDL.tail.prev().item() + " " + DDL.head.next().item());
        }
    }
}
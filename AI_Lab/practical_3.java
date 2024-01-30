import java.util.Scanner;


class practical_3 {

    public static void printMenu() {
            System.out.println("--MENU--");
            System.out.println("1. Selection Sort");
            System.out.println("2. Prim's Minimum Spanning Tree Algorithm");
            System.out.println("3. Kruskal's Minimum Spanning Tree Algorithm");
            System.out.println("4. Job Scheduling Problem");
            System.out.println("5. Dijkstra's Minimal Spanning Tree Algorithm");
            System.out.println("6. Single-Source Shortest Path Problem");
            System.out.println("9. exit");
    }

    public static void printList(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i]);
            System.out.print(" ");
        }
        System.out.println();
    }

    public static void print2D(int[][] arr) {
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr.length; j++) {
                System.out.print(arr[i][j]+" ");
            }
            System.out.println();
        }
        System.out.println();
    }

    public static int[] selection_sort(int list[]) {
        int t;

        for (int i = 0; i < list.length; i++) {
            t = i;
            for (int j = i+1; j < list.length; j++) {
                if(list[t] > list[j]) {
                    t = j;
                }
            }
            int temp = list[i];
            list[i] = list[t];
            list[t] = temp;
        }
        return list;
    }

    public static void prims_algorithm(Scanner s) {
        System.out.print("Enter Number of Nodes");
        int n = s.nextInt();

        int[][] mat = new int[n][n];
        // print2D(mat);

        System.out.print("Enter Number of Edges:");
        int m = s.nextInt();
        for (int i = 0; i < m; i++) {
            System.out.println("Enter Details of Edge "+(i+1)+" as start end weight");
            int start = s.nextInt();
            int end = s.nextInt();
            int weight = s.nextInt();
            mat[start][end] = weight;
            mat[end][start] = weight;
        }

        print2D(mat);

        int[] vis = new int[n];

        
        int[][] tree = new int[n-1][3];
        int t=0,sumw=0;

        for (int i = 0; i < n; i++) {
            if(vis[i] == 1){
                int sv,ev,wv=999;
                boolean flag=false;
                for (int j = 0; j < n; j++) {
                    if(mat[i][j] > 0){
                        if(mat[i][j] < wv && vis[j] != 1){
                            wv = mat[i][j];
                            sv = i;
                            ev = j;
                            flag = true;
                        }
                    }
                }
                if(flag){
                    vis[ev] = 1;
                    tree[t][0] = sv;
                    tree[t][1] = ev;
                    tree[t][2] = wv;
                    sumw += wv;
                }else{
                    break;
                }
            }
        }

        System.out.println("Tree is :");
        print2D(tree);

    }
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int ch=0;
        printMenu();
        while (ch != 9) {
            System.out.print("Enter Your Choice(0 to Display Menu):");
            ch = s.nextInt();
            if(ch == 0){
                printMenu();
                System.out.print("Enter Your Choice:");
                ch = s.nextInt();
            }
            switch (ch) {
                case 1:
                    System.out.println("Enter Number of Elements:");
                    int n = s.nextInt();
                    
                    int[] l = new int[n];

                    System.out.println("Enter Numbers:");
                    for (int i = 0; i < n; i++) {
                        l[i] = s.nextInt();
                    }
                    
                    System.out.print("Original List ");
                    printList(l);

                    int[] newl = selection_sort(l);

                    System.out.print("List After Selection Sort ");
                    printList(newl);
                    break;

                case 2:
                    prims_algorithm(s);
                    break;
                
                case 3:

                    break;
                
                case 4:

                    break;
                
                case 5:

                    break;
                
                case 6:

                    break;
                
                case 7:

                    break;
                
                case 9:
                    System.out.println("Thank You");
                    break;

                default:
                    System.out.println("Invalid Input");
                    break;
            }
        }


    }
}
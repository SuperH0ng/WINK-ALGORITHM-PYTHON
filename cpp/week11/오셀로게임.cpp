#include <iostream>
using namespace std;

int main()
{
    int t, c;
    short x, y, row, col, answerO, answerX;
    bool check;
    cin >> t;

    for (int zzz = 0; zzz < t; zzz++)
    {
        char othello[9][9];
        fill(othello[0], othello[10], '+');

        othello[4][5] = 'X';
        othello[5][4] = 'X';
        othello[4][4] = 'O';
        othello[5][5] = 'O';
        cin >> c;

        short order = 0;
        for (int i = 0; i < c; i++)
        {
            cin >> row >> col;
            char now = (order) ? 'O' : 'X';
            othello[row][col] = now;

            // 왼쪽 위
            x = row;
            y = col;
            check = false;
            while (x >= 2 && y >= 2)
            {
                x--;
                y--;

                if (othello[x][y] == now)
                {
                    check = true;
                    break;
                }
                else if (othello[x][y] == '+')
                {
                    break;
                }
                else
                {
                    continue;
                }
            }
            if (check)
            {
                for (int i = x + 1, j = y + 1; i < row; i++, j++)
                {
                    othello[i][j] = now;
                }
            }

            //오른쪽 위
            x = row;
            y = col;
            check = false;
            while (x >= 2 && y < 8)
            {
                x--;
                y++;

                if (othello[x][y] == now)
                {
                    check = true;
                    break;
                }
                else if (othello[x][y] == '+')
                {
                    break;
                }
                else
                {
                    continue;
                }
            }
            if (check)
            {
                for (int i = x + 1, j = y - 1; i < row; i++, j--)
                {
                    othello[i][j] = now;
                }
            }

            //왼쪽 아래
            x = row;
            y = col;
            check = false;
            while (x < 8 && y >= 2)
            {
                x++;
                y--;

                if (othello[x][y] == now)
                {
                    check = true;
                    break;
                }
                else if (othello[x][y] == '+')
                {
                    break;
                }
                else
                {
                    continue;
                }
            }
            if (check)
            {
                for (int i = x - 1, j = y + 1; i > row; i--, j++)
                {
                    othello[i][j] = now;
                }
            }

            //오른쪽 아래
            x = row;
            y = col;
            check = false;
            while (x < 8 && y < 8)
            {
                x++;
                y++;

                if (othello[x][y] == now)
                {
                    check = true;
                    break;
                }
                else if (othello[x][y] == '+')
                {
                    break;
                }
                else
                {
                    continue;
                }
            }
            if (check)
            {
                for (int i = x - 1, j = y - 1; i > row; i--, j--)
                {
                    othello[i][j] = now;
                }
            }

            //위
            x = row;
            y = col;
            check = false;
            while (x >= 2)
            {
                x--;

                if (othello[x][y] == now)
                {
                    check = true;
                    break;
                }
                else if (othello[x][y] == '+')
                {
                    break;
                }
                else
                {
                    continue;
                }
            }
            if (check)
            {
                for (int i = x + 1; i < row; i++)
                {
                    othello[i][y] = now;
                }
            }

            //아래
            x = row;
            y = col;
            check = false;
            while (x < 8)
            {
                x++;

                if (othello[x][y] == now)
                {
                    check = true;
                    break;
                }
                else if (othello[x][y] == '+')
                {
                    break;
                }
                else
                {
                    continue;
                }
            }
            if (check)
            {
                for (int i = x - 1; i > row; i--)
                {
                    othello[i][y] = now;
                }
            }

            //왼쪽
            x = row;
            y = col;
            check = false;
            while (y >= 2)
            {
                y--;

                if (othello[x][y] == now)
                {
                    check = true;
                    break;
                }
                else if (othello[x][y] == '+')
                {
                    break;
                }
                else
                {
                    continue;
                }
            }
            if (check)
            {
                for (int i = y + 1; i < col; i++)
                {
                    othello[x][i] = now;
                }
            }

            //오른쪽 ㅋㅋㅋㅋㅋㅋㅋㅋ 하드 코딩 끗
            x = row;
            y = col;
            check = false;
            while (y < 8)
            {
                y++;

                if (othello[x][y] == now)
                {
                    check = true;
                    break;
                }
                else if (othello[x][y] == '+')
                {
                    break;
                }
                else
                {
                    continue;
                }
            }
            if (check)
            {
                for (int i = y - 1; i > col; i--)
                {
                    othello[x][i] = now;
                }
            }

            order = 1 - order;
        }

        answerO = 0;
        answerX = 0;

        for (int i = 1; i <= 8; i++)
        {
            for (int j = 1; j <= 8; j++)
            {
                if (othello[i][j] == 'X')
                    answerX++;
                else if (othello[i][j] == 'O')
                    answerO++;
            }
        }

        cout << answerX << " " << answerO << endl;

        for (int i = 1; i <= 8; i++)
        {
            for (int j = 1; j <= 8; j++)
            {
                cout << othello[i][j];
            }
            cout << endl;
        }
    }
}

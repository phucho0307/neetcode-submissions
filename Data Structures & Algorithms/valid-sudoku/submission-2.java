class Solution {
    public boolean isValidSudoku(char[][] board) {
        for(int i=0; i<board.length; i++){            
            for(int j=0; j<board.length-1;j++){
                for(int k=j+1; k<9;k++){
                    if(board[i][j] == board[i][k] && board[i][j] != '.') 
                    return false;
                    if(board[j][i] == board[k][i] && board[j][i] != '.') 
                    return false;
                }
            }
        }

         for (int row = 0; row < 9; row += 3) {
            for (int col = 0; col < 9; col += 3) {
                boolean[] seen = new boolean[10];
                for (int i = row; i < row + 3; i++) {
                    for (int j = col; j < col + 3; j++) {
                        char c = board[i][j];
                        if (c != '.') {
                            int num = c - '0';
                            if (seen[num]) return false;
                            seen[num] = true;
                        }
                    }
                }
            }
        }

        return true;


                        
                    
                    

    }
   
        
    
        
    
}

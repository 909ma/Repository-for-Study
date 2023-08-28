/*
	@Author   : 909ma
	@Date     : 2023. 5. 19
	@Function : 배열 뒤집기 연습
 */
package practice;

public class Java10811LogicTest {

	public static void main(String[] args) {
		int[] zz = {1, 2, 3, 4, 5};
		int[] zzr = {1, 2, 3, 4, 5};
		
		int startNumber = 3;
		int endNumber = 5;
		int start = startNumber-1;
		int end = endNumber-1;
		
		for(int i = 0; i <= end-start; i++) {
			zzr[start + i] = zz[end - i];
		}
		
		for(int i = 0; i < 5 ; i++) {
			System.out.println(zzr[i]);
		}
	}

}

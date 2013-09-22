//kiem thu do vi cho chuong trinh giai phuong trinh bac nhat
public class Test
{
	static int giaiPTB1(int a, int b){
		if (a==0)
		 return 0;
		try{
			return -b/a;
		}catch(Exception e){
			return 0;
		}
		return -b/a;
	}
	static void  test1(){
		int ketQuaThat=giaiPTB1(1,1);
		if(ketQuaThat== -1){
			System.out.println("test1 wass sucess");
			
		}else{
			System.out.println("fail");
		}
	}
	static void static test2(){
		int ketQuaThat=giaiPTB1(10,-90);
		if(ketQuaThat== 9){
			System.out.println("test1 wass sucess");
			
		}else{
			System.out.println("fail");
		}
	}
	static void static test3(){
		int ketQuaThat=giaiPTB1(0,1);
		if(ketQuaThat== 0){
			System.out.println("test1 wass sucess");
			
		}else{
			System.out.println("fail");
		}
	}
	public static void main(String args[])
	{
		System.out.println("fsadfasd");
		int i =giaPTB1(0,1);
		test1();
		test2();
	}
}
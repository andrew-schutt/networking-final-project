/* Simple client to pass strings to the server. 
   Modeled after the simpleserver client code in the text. */

/* Paul Gray 
   Networking F10
   Comments stripped for this sample code...your code should 
   describe what sections play what role. */

import java.io.*;
import java.net.Socket;
import java.net.InetAddress; 

public class SimpleTalkClient {

           static final int SERVER_PORT = 2024;
           static final int MAX_LINE = 256;
           private static PrintStream ps;	
	   private static Socket sock;
	   private static String hostname = "";
	  

           public static void main(String args []) {

     
                if(args.length == 1) {
                   
                    hostname = args[0];
                        
                }
                else {
                	System.err.println("Usage: java SimpleTalkClient [host]");
                        System.exit(1);
                }//endif
	    
                try{
			sock = new Socket(InetAddress.getByName(hostname), SERVER_PORT); 
	                System.out.println("connected to " +  
					InetAddress.getByName(hostname).getHostName() 
					   + " on " + "port " + SERVER_PORT);    
		        
		        BufferedReader bufftype = new BufferedReader(
							new InputStreamReader(System.in));
			ps = new PrintStream(
					sock.getOutputStream());
	 		try{
                               String teletype = "";
				 
				do {
                                   
				   System.out.print("write> ");
				   System.out.flush();
				   teletype = bufftype.readLine().trim();
				  
                                   ps.println(teletype);                                  
                                   
         			}while(!teletype.equals("exit"));//endwhile
				  
                            }catch(Exception e) {System.out.println(e);
                                                    
                                                    closeConnections();
                                                             
                                                   }
                            finally { closeConnections(); }
                
		}catch(IOException ioe) { System.out.println("SimpleTalk: unknown host: " 
	           				  + hostname);}
                   
		}//endmain

   
		public static void closeConnections() {

                      try {
                             ps.close();
                             sock.close();
                             System.exit(0);
 
                      }catch(Exception e) {System.out.println(e);}//endtry


		}//endcloseConnections

}//endSimpleTalkClient


/* Real simple server modeled after the book's simpleserver server program. */

/* Paul Gray 
   Networking F10
   Comments stripped for this sample code...your code should 
   describe what sections play what role. */

import java.net.ServerSocket;
import java.net.Socket;
import java.net.InetAddress;
import java.io.*;

public class SimpleTalkServer
{

  static final int SERVER_PORT = 2024;
  static final int MAX_PENDING = 5;
  static final int MAX_LINE = 256;
  private static ServerSocket ssock;
  private static Socket sock;

  public static void main (String[]args)
  {

    if (args.length > 0)
      {

	System.err.println ("Usage: [filename]");
	System.exit (0);

      }

    try
    {
      ssock = new ServerSocket (SERVER_PORT, MAX_PENDING);
      while (true)
	{
	  try
	  {
	    System.out.println ("host: "
				+ InetAddress.getLocalHost ().getHostName ());
	    System.out.println ("listening for clients on port " +
				SERVER_PORT + "....");
	    sock = ssock.accept ();
	    System.out.println ("Connected to " +
				sock.getInetAddress ().getHostName ());
	    try
	    {

	      BufferedReader in =
		new BufferedReader (new
				    InputStreamReader (sock.
						       getInputStream ()));
	      String teletype = "";
	      do
		{
		  teletype = in.readLine ().trim ();
		  System.out.println ("client@" +
				      sock.getInetAddress ().getHostName ()
				      + "> " + teletype);
		}
	      while (!teletype.equals ("exit"));	//endwhile          
	    }
	    catch (Exception e1)
	    {
	      System.out.println (e1);
	    }			//endtry

	  }
	  catch (Exception e2)
	  {
	    System.out.println (e2);
	  }			//endtry

	}			//endwhile
    }
    catch (IOException ioe)
    {
      System.out.println (ioe);
    }				//endtry
  }				//endmain
}				//end SimpleTalkServer

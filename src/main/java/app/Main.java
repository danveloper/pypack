package app;

import javax.script.ScriptEngine;
import javax.script.ScriptEngineManager;
import java.io.InputStream;

public class Main {

  public static void main(String[] args) throws Exception {
    ScriptEngine engine = new ScriptEngineManager().getEngineByName("jython");
    InputStream scriptStream = Main.class.getResourceAsStream("/ratpack.py");
    byte[] bytes = new byte[scriptStream.available()];
    scriptStream.read(bytes);
    engine.eval(new String(bytes));
  }
}

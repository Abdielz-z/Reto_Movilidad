// Root myDeserializedClass = JsonConvert.DeserializeObject<Root>(myJsonResponse);
    public class Carros
    {
        public int cantidad { get; set; }
        public List<List<List<float>>> posiciones { get; set; }
    }

    public class Sem
    {
        public int id { get; set; }
        public List<int> estados { get; set; }
    }

    public class Semaforos
    {
        public Sem sem1 { get; set; }
        public Sem sem2 { get; set; }
        public Sem sem3 { get; set; }
        public Sem sem4 { get; set; }
        public Sem sem5 { get; set; }
        public Sem sem6 { get; set; }
        public Sem sem7 { get; set; }
        public Sem sem8 { get; set; }
        public Sem sem9 { get; set; }
        public Sem sem10 { get; set; }
        public Sem sem11 { get; set; }
        public Sem sem12 { get; set; }
    }

public class Dicc
    {
        public Carros carros { get; set; }
        public Semaforos semaforos { get; set; }
    }

    public class Root
    {
        public Dicc dicc { get; set; }
    }
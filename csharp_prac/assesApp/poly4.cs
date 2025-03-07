using System;

class Animal
{
    public virtual void sound()
    {
      
    }
}

class Dog : Animal
{
    public override void sound()
    {
        Console.WriteLine("Bow Bow");
    }
}

class Duck : Animal
{
    public new void sound()
    {
        Console.WriteLine("Quack Quack");
    }
}

class Cat : Animal
{
    public override void sound()
    {
        Console.WriteLine("Meow Meow");
    }
}

class poly4
{
    public static void Main(string[] args)
    {
        Animal obj = new Animal();
        Animal dog = new Dog();
        Animal cat = new Cat();
        Animal duck = new Cat();

        dog.sound();
        cat.sound();
        duck.sound();
    }
}
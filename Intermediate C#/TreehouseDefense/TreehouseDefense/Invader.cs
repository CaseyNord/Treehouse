﻿namespace TreehouseDefense
{
   abstract class Invader : IInvader
   {
      private readonly Path _path;
      // Keeps track of Invader's location. 
      private int _pathStep = 0;
       
      protected virtual int StepSize { get; } = 1; 
      
      // Gets location of Invader based on its path step. 
      public MapLocation Location => _path.GetLocationAt(_pathStep);
       
      public abstract int Health { get; protected set; }
      
      // True if the invader has reached the end of the path. 
      public bool HasScored { get { return _pathStep >= _path.Length; } }
      
      public bool IsNeutralized => Health <= 0;

      public bool IsActive => !(IsNeutralized || HasScored);
             
      public Invader(Path path)
      {
         _path = path;
      }
       
      public void Move() => _pathStep += StepSize;
      
      public virtual void DecreaseHealth(int factor)
      {
         Health -= factor;
         System.Console.WriteLine("Shot at and hit an invader!"); 
      }
   }
}

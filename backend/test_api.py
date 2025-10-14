#!/usr/bin/env python3
"""
Test script to verify the Task Tracker API works correctly.
This uses SQLite instead of PostgreSQL for easy testing.
"""

import sys
import os

# Use test database configuration
os.environ['DATABASE_URL'] = 'sqlite:///./test_tasktracker.db'

# Import after setting environment variable
from app.database import SessionLocal, engine, Base
from app.models import Task
from app.schemas import TaskCreate

def test_database():
    """Test database operations"""
    print("Testing database operations...")
    
    # Create tables
    Base.metadata.create_all(bind=engine)
    print("✓ Database tables created")
    
    # Create a session
    db = SessionLocal()
    
    try:
        # Create a task
        task_data = TaskCreate(
            title="Test Task",
            description="This is a test task",
            completed=False
        )
        db_task = Task(**task_data.dict())
        db.add(db_task)
        db.commit()
        db.refresh(db_task)
        print(f"✓ Created task: {db_task.title} (ID: {db_task.id})")
        
        # Get all tasks
        tasks = db.query(Task).all()
        print(f"✓ Retrieved {len(tasks)} task(s)")
        
        # Update task
        db_task.completed = True
        db.commit()
        print(f"✓ Updated task to completed: {db_task.completed}")
        
        # Delete task
        db.delete(db_task)
        db.commit()
        print("✓ Deleted task")
        
        print("\n✅ All database tests passed!")
        return True
        
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        return False
    finally:
        db.close()
        # Clean up test database
        if os.path.exists('test_tasktracker.db'):
            os.remove('test_tasktracker.db')

if __name__ == "__main__":
    success = test_database()
    sys.exit(0 if success else 1)

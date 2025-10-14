'use client';

import { Task } from '../types';
import { updateTask, deleteTask } from '../api';

interface TaskItemProps {
  task: Task;
  onUpdate: () => void;
}

export default function TaskItem({ task, onUpdate }: TaskItemProps) {
  const handleToggle = async () => {
    try {
      await updateTask(task.id, { completed: !task.completed });
      onUpdate();
    } catch (error) {
      console.error('Failed to update task:', error);
    }
  };

  const handleDelete = async () => {
    try {
      await deleteTask(task.id);
      onUpdate();
    } catch (error) {
      console.error('Failed to delete task:', error);
    }
  };

  return (
    <div className="flex items-center gap-3 p-4 bg-white dark:bg-gray-800 rounded-lg shadow-sm border border-gray-200 dark:border-gray-700">
      <input
        type="checkbox"
        checked={task.completed}
        onChange={handleToggle}
        className="w-5 h-5 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600"
      />
      <div className="flex-1">
        <h3 className={`font-medium ${task.completed ? 'line-through text-gray-400' : 'text-gray-900 dark:text-white'}`}>
          {task.title}
        </h3>
        {task.description && (
          <p className={`text-sm ${task.completed ? 'line-through text-gray-400' : 'text-gray-600 dark:text-gray-400'}`}>
            {task.description}
          </p>
        )}
      </div>
      <button
        onClick={handleDelete}
        className="px-3 py-1 text-sm text-red-600 hover:text-red-800 dark:text-red-400 dark:hover:text-red-300 font-medium"
      >
        Delete
      </button>
    </div>
  );
}

'use client';

import { Task } from '../types';
import TaskItem from './TaskItem';

interface TaskListProps {
  tasks: Task[];
  onUpdate: () => void;
}

export default function TaskList({ tasks, onUpdate }: TaskListProps) {
  if (tasks.length === 0) {
    return (
      <div className="text-center py-12">
        <p className="text-gray-500 dark:text-gray-400">No tasks yet. Create your first task above!</p>
      </div>
    );
  }

  return (
    <div className="space-y-3">
      {tasks.map((task) => (
        <TaskItem key={task.id} task={task} onUpdate={onUpdate} />
      ))}
    </div>
  );
}

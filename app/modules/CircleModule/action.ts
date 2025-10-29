import type { ActionFunctionArgs } from "react-router";

export async function CircleAction({ request }: ActionFunctionArgs) {
  const formData = await request.formData();
  const radius = formData.get('radius');

  // Simulate API call to backend
  const response = await fetch('https://jsonplaceholder.typicode.com/posts', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      radius,
      formula: 'π * radius * radius',
    }),
  });

  if (!response.ok) {
    return { success: false, error: 'Failed to calculate' };
  }

  // Calculate area (π * r^2)
  const area = Math.PI * Number(radius) * Number(radius);

  return { success: true, result: parseFloat(area.toFixed(2)) };
}


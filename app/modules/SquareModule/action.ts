import type { ActionFunctionArgs } from "react-router";

export async function SquareAction({ request }: ActionFunctionArgs) {
  const formData = await request.formData();
  const side = formData.get('side');

  // Call AWS API
  const response = await fetch('https://t7ow9idud3.execute-api.us-east-1.amazonaws.com/square-surface/calculate', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      side: Number(side),
    }),
  });

  if (!response.ok) {
    return { success: false, error: 'Failed to calculate' };
  }

  const data = await response.json();

  return { success: true, result: data.surface_area };
}


import { useState, useEffect } from 'react';

export const useCountdown = (targetDate) => {
  const [countdown, setCountdown] = useState(calculateCountdown(targetDate));

  useEffect(() => {
    if (!targetDate) return;

    const interval = setInterval(() => {
      setCountdown(calculateCountdown(targetDate));
    }, 1000);

    return () => clearInterval(interval);
  }, [targetDate]);

  return countdown;
};

function calculateCountdown(targetDate) {
  if (!targetDate) {
    return { days: 0, hours: 0, minutes: 0, seconds: 0, isValid: false };
  }

  const now = new Date().getTime();
  const target = new Date(targetDate).getTime();
  const difference = target - now;

  if (difference < 0) {
    return { days: 0, hours: 0, minutes: 0, seconds: 0, isValid: false };
  }

  const days = Math.floor(difference / (1000 * 60 * 60 * 24));
  const hours = Math.floor((difference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  const minutes = Math.floor((difference % (1000 * 60 * 60)) / (1000 * 60));
  const seconds = Math.floor((difference % (1000 * 60)) / 1000);

  return { days, hours, minutes, seconds, isValid: true };
}
